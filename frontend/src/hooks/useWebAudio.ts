"use client";

import { useCallback, useRef } from "react";

export function useWebAudio() {
  const audioCtxRef = useRef<AudioContext | null>(null);

  const getAudioContext = useCallback((): AudioContext | null => {
    if (typeof window === "undefined") return null;

    if (!audioCtxRef.current) {
      const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
      if (AudioCtx) {
        audioCtxRef.current = new AudioCtx();
      }
    }

    if (audioCtxRef.current && audioCtxRef.current.state === "suspended") {
      audioCtxRef.current.resume().catch(() => {});
    }

    return audioCtxRef.current;
  }, []);

  /**
   * 880Hz -> 1174Hz Sine Wave sweep for 300ms.
   * Played when a new order ticket arrives at KDS.
   */
  const playNewTicketSound = useCallback(() => {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;

      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(880, now);
      osc.frequency.exponentialRampToValueAtTime(1174, now + 0.3);

      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.3);
    } catch (err) {
      console.warn("[WebAudio] Audio synthesis not permitted without user gesture:", err);
    }
  }, [getAudioContext]);

  /**
   * 440Hz Square Wave with 3 pulses for overdue SLA (> 5 minutes).
   */
  const playOverdueAlertSound = useCallback(() => {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;

      const now = ctx.currentTime;
      const pulses = [0, 0.2, 0.4];

      pulses.forEach((timeOffset) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = "square";
        osc.frequency.setValueAtTime(440, now + timeOffset);

        gain.gain.setValueAtTime(0.2, now + timeOffset);
        gain.gain.exponentialRampToValueAtTime(0.01, now + timeOffset + 0.15);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now + timeOffset);
        osc.stop(now + timeOffset + 0.15);
      });
    } catch (err) {
      console.warn("[WebAudio] Audio synthesis failed:", err);
    }
  }, [getAudioContext]);

  /**
   * 587Hz Sine Wave chime for 500ms for Customer table service request bell.
   */
  const playServiceCallSound = useCallback(() => {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;

      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(587, now);

      gain.gain.setValueAtTime(0.25, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.5);
    } catch (err) {
      console.warn("[WebAudio] Audio synthesis failed:", err);
    }
  }, [getAudioContext]);

  return {
    playNewTicketSound,
    playOverdueAlertSound,
    playServiceCallSound,
  };
}
