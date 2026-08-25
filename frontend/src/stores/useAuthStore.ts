import { create } from "zustand";
import { UserRole } from "@/types";

interface AuthState {
  token: string | null;
  username: string | null;
  role: UserRole | null;
  branchId: string | null;
  isAuthenticated: boolean;
  login: (token: string, username: string, role: UserRole, branchId?: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: null,
  username: null,
  role: null,
  branchId: null,
  isAuthenticated: false,
  login: (token, username, role, branchId) =>
    set({
      token,
      username,
      role,
      branchId: branchId || null,
      isAuthenticated: true,
    }),
  logout: () =>
    set({
      token: null,
      username: null,
      role: null,
      branchId: null,
      isAuthenticated: false,
    }),
}));
