import { create } from "zustand";
import { UserProfile, UserRole } from "@/types";

interface AuthState {
  token: string | null;
  refreshToken: string | null;
  user: UserProfile | null;
  isAuthenticated: boolean;
  
  // Actions
  login: (tokens: { accessToken: string; refreshToken: string }, user: UserProfile) => void;
  logout: () => void;
  updateUser: (partialUser: Partial<UserProfile>) => void;
  setToken: (token: string) => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: typeof window !== "undefined" ? localStorage.getItem("smart_fb_token") : null,
  refreshToken: typeof window !== "undefined" ? localStorage.getItem("smart_fb_refresh_token") : null,
  user: null,
  isAuthenticated: false,

  login: (tokens, user) => {
    if (typeof window !== "undefined") {
      localStorage.setItem("smart_fb_token", tokens.accessToken);
      localStorage.setItem("smart_fb_refresh_token", tokens.refreshToken);
    }
    set({
      token: tokens.accessToken,
      refreshToken: tokens.refreshToken,
      user,
      isAuthenticated: true,
    });
  },

  logout: () => {
    if (typeof window !== "undefined") {
      localStorage.removeItem("smart_fb_token");
      localStorage.removeItem("smart_fb_refresh_token");
    }
    set({
      token: null,
      refreshToken: null,
      user: null,
      isAuthenticated: false,
    });
  },

  updateUser: (partialUser) =>
    set((state) => ({
      user: state.user ? { ...state.user, ...partialUser } : null,
    })),

  setToken: (token) => {
    if (typeof window !== "undefined") {
      localStorage.setItem("smart_fb_token", token);
    }
    set({ token, isAuthenticated: !!token });
  },
}));
