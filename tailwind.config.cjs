/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Menlo', 'Monaco', 'monospace'],
      },
      colors: {
        culinary: '#f97316',
        cinema: '#a855f7',
        travel: '#06b6d4',
      }
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        night: {
          "primary": "#f59e0b",
          "primary-content": "#0f1117",
          "secondary": "#38bdf8",
          "accent": "#f43f5e",
          "neutral": "#1f2430",
          "neutral-content": "#cbd5e1",
          "base-100": "#0c0e14",
          "base-200": "#131620",
          "base-300": "#1b202e",
          "base-content": "#e2e8f0",
          "info": "#38bdf8",
          "success": "#10b981",
          "warning": "#f59e0b",
          "error": "#ef4444",
        },
        light: {
          "primary": "#d97706",
          "primary-content": "#ffffff",
          "secondary": "#0284c7",
          "accent": "#e11d48",
          "neutral": "#e7e2d8",
          "neutral-content": "#1c1917",
          "base-100": "#faf8f5",
          "base-200": "#f3eee5",
          "base-300": "#e6ded1",
          "base-content": "#1e293b",
          "info": "#0284c7",
          "success": "#059669",
          "warning": "#d97706",
          "error": "#dc2626",
        }
      }
    ],
    darkTheme: "night",
    logs: false,
  }
}
