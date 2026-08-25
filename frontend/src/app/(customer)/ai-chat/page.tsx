"use client";

import Link from "next/link";
import { ArrowLeft, Sparkles, Send } from "lucide-react";
import { useState } from "react";

export default function AiChatPage() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Xin chào! Tôi là Trợ lý Ảo AI của quán. Bạn muốn tìm đồ uống hợp khẩu vị, ít ngọt, hoặc gợi ý combo hôm nay?",
    },
  ]);

  const handleSend = () => {
    if (!input.trim()) return;
    const newMsg = { role: "user", content: input };
    setMessages((prev) => [
      ...prev,
      newMsg,
      { role: "assistant", content: `Gợi ý cho bạn: Trà Đào Cam Sả hoặc Cà Phê Muối Hoàng Gia đang là 'Best Seller' được nhiều khách ưa thích nhất hôm nay!` },
    ]);
    setInput("");
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 max-w-md mx-auto flex flex-col justify-between">
      <header className="flex items-center gap-2 py-2 border-b border-slate-200">
        <Link href="/menu" className="p-2 rounded-full hover:bg-slate-200 text-slate-600">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div className="flex items-center gap-2">
          <div className="p-1.5 rounded-lg bg-purple-100 text-purple-600">
            <Sparkles className="w-4 h-4" />
          </div>
          <div>
            <h1 className="text-base font-bold text-slate-900">AI Barista Assistant</h1>
            <p className="text-[11px] text-slate-500">Tư vấn món thông minh (Google Gemini)</p>
          </div>
        </div>
      </header>

      <div className="flex-1 py-4 space-y-3 overflow-y-auto">
        {messages.map((m, idx) => (
          <div
            key={idx}
            className={`p-3 rounded-2xl text-xs max-w-[85%] ${
              m.role === "user"
                ? "ml-auto bg-orange-500 text-white rounded-br-none shadow-sm"
                : "bg-white text-slate-800 border border-slate-200 rounded-bl-none shadow-sm"
            }`}
          >
            {m.content}
          </div>
        ))}
      </div>

      <div className="flex gap-2 pt-2 border-t border-slate-200">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Hỏi AI tư vấn đồ uống..."
          className="flex-1 text-xs px-3 py-2.5 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-purple-500 bg-white"
        />
        <button
          onClick={handleSend}
          className="p-2.5 rounded-xl bg-purple-600 hover:bg-purple-700 text-white shadow-sm"
        >
          <Send className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
