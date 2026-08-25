"use client";

import React, { useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Star, Upload, X, CheckCircle2, ShieldAlert, ArrowLeft } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Textarea } from "@/components/ui/Textarea";
import { Switch } from "@/components/ui/Switch";
import { compressImageToWebP } from "@/lib/utils";

export default function OrderReviewPage() {
  const params = useParams();
  const router = useRouter();
  const orderId = (params?.orderId as string) || "ORD-0042";

  const [rating, setRating] = useState<number>(5);
  const [selectedTags, setSelectedTags] = useState<string[]>([]);
  const [comment, setComment] = useState("");
  const [isAnonymous, setIsAnonymous] = useState(false);
  const [uploadedImages, setUploadedImages] = useState<string[]>([]);
  const [isUploading, setIsUploading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const availableTags = [
    "Pha chế nhanh",
    "Đồ uống thơm ngon",
    "Nhân viên nhiệt tình",
    "Không gian sạch đẹp",
    "Đóng gói cẩn thận",
    "Đúng định lượng đá/đường",
  ];

  const ratingDescriptions: Record<number, { text: string; color: string }> = {
    1: { text: "Rất không hài lòng (Kích hoạt Red Alert)", color: "text-rose-600" },
    2: { text: "Chưa hài lòng (Kích hoạt Red Alert)", color: "text-rose-500" },
    3: { text: "Bình thường / Tạm được", color: "text-amber-600" },
    4: { text: "Hài lòng & chất lượng tốt", color: "text-emerald-600" },
    5: { text: "Tuyệt vời & rất thích!", color: "text-emerald-700 font-extrabold" },
  };

  const handleToggleTag = (tag: string) => {
    setSelectedTags((prev) =>
      prev.includes(tag) ? prev.filter((t) => t !== tag) : [...prev, tag]
    );
  };

  const handleImageUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (!files || files.length === 0) return;

    if (uploadedImages.length + files.length > 3) {
      alert("Quý khách chỉ có thể tải lên tối đa 3 hình ảnh");
      return;
    }

    setIsUploading(true);
    try {
      const promises = Array.from(files).map((file) => compressImageToWebP(file));
      const results = await Promise.all(promises);
      setUploadedImages((prev) => [...prev, ...results.map((r) => r.base64)]);
    } catch (err) {
      console.error("Compression error:", err);
    } finally {
      setIsUploading(false);
    }
  };

  const handleRemoveImage = (index: number) => {
    setUploadedImages((prev) => prev.filter((_, idx) => idx !== index));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    const payload = {
      orderId,
      rating,
      tags: selectedTags,
      comment,
      isAnonymous,
      imagesBase64: uploadedImages,
      isRedAlert: rating <= 2, // Red Alert protocol for <= 2 stars
    };

    setTimeout(() => {
      setIsSubmitting(false);
      setIsSubmitted(true);
    }, 800);
  };

  if (isSubmitted) {
    return (
      <div className="px-4 py-16 text-center space-y-4">
        <CheckCircle2 className="h-16 w-16 text-emerald-600 mx-auto animate-bounce" />
        <h3 className="text-xl font-black text-slate-900">Cảm Ơn Đánh Giá Của Bạn!</h3>
        <p className="text-xs text-slate-500 max-w-xs mx-auto">
          {rating <= 2
            ? "Chúng tôi vô cùng xin lỗi về trải nghiệm chưa tốt. Quản lý cửa hàng đã nhận được thông báo khẩn cấp và sẽ phản hồi trong 3 phút."
            : "Ý kiến đóng góp quý báu của bạn giúp Smart F&B không ngừng nâng cao chất lượng phục vụ mỗi ngày."}
        </p>
        <Button onClick={() => router.push("/menu")} variant="primary" className="mt-4">
          Quay Lại Thực Đơn
        </Button>
      </div>
    );
  }

  return (
    <div className="space-y-6 px-4 pt-4 pb-12">
      {/* Header */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={() => router.back()}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Quay lại đơn hàng</span>
        </button>
        <span className="text-xs font-bold text-slate-500">Mã Đơn: #{orderId}</span>
      </div>

      <div className="space-y-1">
        <h2 className="text-xl font-black text-slate-950">Đánh Giá Trải Nghiệm</h2>
        <p className="text-xs text-slate-500">
          Hãy cho chúng tôi biết cảm nhận thực tế của bạn về chất lượng đồ uống và dịch vụ.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-5">
        {/* 1-5 Star Rating Card */}
        <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm text-center space-y-3">
          <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
            Chấm Điểm Sao (1 - 5 Sao)
          </label>

          <div className="flex items-center justify-center gap-2 py-2">
            {[1, 2, 3, 4, 5].map((star) => (
              <button
                key={star}
                type="button"
                onClick={() => setRating(star)}
                className="p-1 text-slate-300 hover:scale-125 transition-transform"
              >
                <Star
                  className={`h-9 w-9 ${
                    star <= rating
                      ? "text-amber-500 fill-amber-500"
                      : "text-slate-200 fill-slate-100"
                  }`}
                />
              </button>
            ))}
          </div>

          <p className={`text-xs font-bold ${ratingDescriptions[rating]?.color}`}>
            {ratingDescriptions[rating]?.text}
          </p>

          {/* Red Alert Warning */}
          {rating <= 2 && (
            <div className="bg-rose-50 border border-rose-200 rounded-2xl p-3 text-xs text-rose-900 flex items-start gap-2 text-left">
              <ShieldAlert className="h-5 w-5 text-rose-600 shrink-0" />
              <div>
                <span className="font-bold block">Kích Hoạt Cảnh Báo Khẩn Cấp (Red Alert)</span>
                <p className="text-[11px] mt-0.5">
                  Đánh giá này sẽ kích hoạt thông báo rung chuông ngay lập tức tới Quản lý chi nhánh để hỗ trợ xử lý tại bàn.
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Quick Feeling Tags */}
        <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
          <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
            Nhãn Cảm Nhận Nhanh
          </label>
          <div className="flex flex-wrap gap-2">
            {availableTags.map((tag) => {
              const isSelected = selectedTags.includes(tag);
              return (
                <button
                  key={tag}
                  type="button"
                  onClick={() => handleToggleTag(tag)}
                  className={`px-3 py-1.5 rounded-full text-xs font-semibold border transition-colors ${
                    isSelected
                      ? "border-amber-700 bg-amber-700 text-white shadow-xs"
                      : "border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-700"
                  }`}
                >
                  {tag}
                </button>
              );
            })}
          </div>
        </div>

        {/* Comment Textarea */}
        <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
          <Textarea
            label="Chi tiết cảm nhận của bạn"
            placeholder="Hãy chia sẻ thêm về hương vị đồ uống, độ ngọt, thái độ phục vụ..."
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            rows={3}
          />

          {/* Photo Upload (Max 3, WebP Compressed) */}
          <div className="space-y-2 pt-2">
            <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
              Đính Kèm Ảnh Thực Tế (Tối đa 3 ảnh WebP)
            </label>

            <div className="flex items-center gap-3">
              {uploadedImages.map((imgBase64, idx) => (
                <div
                  key={idx}
                  className="relative w-20 h-20 rounded-xl overflow-hidden border border-slate-200 shadow-2xs"
                >
                  <img src={imgBase64} alt="Review" className="w-full h-full object-cover" />
                  <button
                    type="button"
                    onClick={() => handleRemoveImage(idx)}
                    className="absolute top-1 right-1 p-1 bg-black/60 text-white rounded-full hover:bg-black"
                  >
                    <X className="h-3 w-3" />
                  </button>
                </div>
              ))}

              {uploadedImages.length < 3 && (
                <label className="w-20 h-20 rounded-xl border-2 border-dashed border-slate-300 hover:border-amber-600 bg-slate-50 flex flex-col items-center justify-center cursor-pointer text-slate-400 hover:text-amber-700 transition-colors">
                  <Upload className="h-5 w-5" />
                  <span className="text-[10px] font-bold mt-1">Tải ảnh</span>
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageUpload}
                    className="hidden"
                    disabled={isUploading}
                  />
                </label>
              )}
            </div>
            {isUploading && (
              <p className="text-[11px] text-amber-700">Đang nén ảnh sang chuẩn WebP...</p>
            )}
          </div>

          {/* Anonymous Toggle */}
          <div className="pt-3 border-t border-slate-100">
            <Switch
              label="Đánh giá ẩn danh"
              description="Ẩn số điện thoại và tên hiển thị công khai trên menu"
              checked={isAnonymous}
              onCheckedChange={setIsAnonymous}
            />
          </div>
        </div>

        {/* Submit Review CTA */}
        <Button
          type="submit"
          isLoading={isSubmitting}
          size="lg"
          variant="primary"
          className="w-full font-bold shadow-md"
        >
          Gửi Đánh Giá Của Tôi
        </Button>
      </form>
    </div>
  );
}
