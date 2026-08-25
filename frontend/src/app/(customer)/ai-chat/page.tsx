"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { useCartStore } from "@/stores/useCartStore";
import { formatCurrencyVND } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import {
  Sparkles,
  Send,
  Coffee,
  ArrowLeft,
  ShoppingBag,
  Check,
  Bot,
  User,
} from "lucide-react";

interface ChatMessage {
  id: string;
  sender: "user" | "ai";
  text: string;
  recommendedProduct?: {
    id: string;
    name: string;
    price: number;
    sizeName: string;
    description: string;
    imageUrl: string;
  };
}

export default function AiChatPage() {
  const router = useRouter();
  const addItem = useCartStore((state) => state.addItem);
  const itemsCount = useCartStore((state) => state.getTotalItemsCount());

  const [inputPrompt, setInputPrompt] = useState("");
  const [isThinking, setIsThinking] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: "msg-01",
      sender: "ai",
      text: "Xin chào quý khách! Tôi là AI Gemini Barista của Smart F&B. Hôm nay thời tiết Sài Gòn khoảng 32°C khá oi bức, bạn đang tìm đồ uống giải nhiệt, thanh mát hay cần một ly cà phê đậm đà để tỉnh táo làm việc?",
    },
  ]);

  const quickPrompts = [
    "Cần tỉnh táo làm việc, ít ngọt",
    "Trà trái cây giải nhiệt mùa hè",
    "Đồ uống béo ngậy, ít cafein",
    "Gợi ý món bán chạy nhất",
  ];

  const handleSend = (textToSend?: string) => {
    const text = textToSend || inputPrompt;
    if (!text.trim()) return;

    const userMsg: ChatMessage = {
      id: `msg-${Date.now()}`,
      sender: "user",
      text: text.trim(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputPrompt("");
    setIsThinking(true);

    setTimeout(() => {
      setIsThinking(false);
      let aiReply: ChatMessage;

      if (text.toLowerCase().includes("tỉnh táo") || text.toLowerCase().includes("cà phê")) {
        aiReply = {
          id: `msg-${Date.now() + 1}`,
          sender: "ai",
          text: "Để tập trung cao độ mà vẫn êm dịu, tôi gợi ý bạn thử **Cà Phê Muối Hoàng Gia** với lớp kem muối béo nhẹ giúp cân bằng vị đắng đậm của Robusta Đắk Lắk!",
          recommendedProduct: {
            id: "prod-01",
            name: "Cà Phê Muối Hoàng Gia",
            price: 35000,
            sizeName: "M",
            description: "Cà phê Robusta đậm vị, kem muối béo thủ công.",
            imageUrl: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400&q=80",
          },
        };
      } else {
        aiReply = {
          id: `msg-${Date.now() + 1}`,
          sender: "ai",
          text: "Một lựa chọn tuyệt vời cho ngày nắng nóng! Ly **Trà Đào Cam Sả Tươi** với cốt trà đen ủ lạnh và đào miếng giòn ngọt sẽ giúp bạn sảng khoái ngay tức thì!",
          recommendedProduct: {
            id: "prod-02",
            name: "Trà Đào Cam Sả Tươi",
            price: 39000,
            sizeName: "M",
            description: "Trà đen ủ lạnh, đào miếng giòn, tinh dầu sả tươi.",
            imageUrl: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
          },
        };
      }

      setMessages((prev) => [...prev, aiReply]);
    }, 700);
  };

  const handleAddRecommended = (prod: ChatMessage["recommendedProduct"]) => {
    if (!prod) return;
    addItem({
      productId: prod.id,
      productName: prod.name,
      imageUrl: prod.imageUrl,
      sizeId: "default-size",
      sizeName: prod.sizeName,
      unitPrice: prod.price,
      quantity: 1,
      sugarLevel: "70%",
      iceLevel: "100%",
      toppings: [],
    });
  };

  return (
    <div className="flex flex-col h-[calc(100vh-64px)] px-4 pt-4 pb-4 max-w-md mx-auto">
      {/* Top Header */}
      <div className="flex items-center justify-between border-b border-slate-200 pb-3">
        <button
          type="button"
          onClick={() => router.back()}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Quay lại</span>
        </button>
        <div className="flex items-center gap-1.5 text-xs font-bold text-amber-800 bg-amber-50 px-3 py-1 rounded-full border border-amber-200">
          <Sparkles className="h-3.5 w-3.5" />
          <span>AI-1 Gemini Barista</span>
        </div>
      </div>

      {/* Chat Messages Log */}
      <div className="flex-1 overflow-y-auto py-4 space-y-4 pr-1">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex items-start gap-2.5 ${
              msg.sender === "user" ? "flex-row-reverse" : "flex-row"
            }`}
          >
            <div
              className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 ${
                msg.sender === "user"
                  ? "bg-slate-800 text-white"
                  : "bg-amber-700 text-white shadow-xs"
              }`}
            >
              {msg.sender === "user" ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
            </div>

            <div
              className={`max-w-[80%] rounded-2xl p-3.5 text-xs leading-relaxed space-y-3 ${
                msg.sender === "user"
                  ? "bg-amber-700 text-white rounded-tr-none font-medium"
                  : "bg-white border border-slate-200 text-slate-800 shadow-2xs rounded-tl-none"
              }`}
            >
              <p>{msg.text}</p>

              {/* Interactive Product Suggestion Card */}
              {msg.recommendedProduct && (
                <div className="bg-amber-50/80 border border-amber-200/90 rounded-xl p-3 text-slate-900 space-y-2">
                  <div className="flex items-center gap-2.5">
                    <img
                      src={msg.recommendedProduct.imageUrl}
                      alt={msg.recommendedProduct.name}
                      className="w-12 h-12 rounded-lg object-cover border border-slate-200 shrink-0"
                    />
                    <div>
                      <h5 className="font-bold text-xs leading-tight">
                        {msg.recommendedProduct.name}
                      </h5>
                      <span className="font-extrabold text-amber-800 text-xs mt-0.5 block">
                        {formatCurrencyVND(msg.recommendedProduct.price)}
                      </span>
                    </div>
                  </div>

                  <Button
                    type="button"
                    onClick={() => handleAddRecommended(msg.recommendedProduct)}
                    size="sm"
                    variant="primary"
                    className="w-full font-bold shadow-xs min-h-[36px]"
                    leftIcon={<ShoppingBag className="h-3.5 w-3.5" />}
                  >
                    Thêm Nhanh Vào Giỏ Hàng
                  </Button>
                </div>
              )}
            </div>
          </div>
        ))}

        {isThinking && (
          <div className="flex items-center gap-2 text-xs text-amber-800 italic bg-amber-50 p-2.5 rounded-xl border border-amber-200 w-max animate-pulse">
            <Sparkles className="h-4 w-4 animate-spin" />
            <span>AI Gemini đang phân tích khẩu vị & thời tiết...</span>
          </div>
        )}
      </div>

      {/* Quick Prompts Suggestions */}
      <div className="flex gap-1.5 overflow-x-auto pb-2 no-scrollbar">
        {quickPrompts.map((qp, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => handleSend(qp)}
            className="px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 hover:text-amber-900 text-[11px] font-semibold text-slate-700 whitespace-nowrap border border-slate-200 shrink-0 transition-colors"
          >
            {qp}
          </button>
        ))}
      </div>

      {/* Input Form */}
      <div className="flex gap-2 pt-1 border-t border-slate-200">
        <input
          type="text"
          value={inputPrompt}
          onChange={(e) => setInputPrompt(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Hỏi AI: 'Trà nào ít ngọt?', 'Món mới...' "
          className="flex-1 px-3.5 py-2.5 text-xs rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-amber-600 bg-white"
        />
        <Button
          type="button"
          onClick={() => handleSend()}
          variant="primary"
          size="md"
          className="shrink-0"
        >
          <Send className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
