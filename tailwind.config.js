/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./*.{html,js}"],
    theme: {
        extend: {
            colors: {
                brand: {
                    blue: {
                        DEFAULT: '#0056b3', // Primary blue
                        dark: '#003d80',
                        light: '#337ab7',
                        50: '#e6f0fa',
                        100: '#cce0f5',
                        200: '#99c2eb',
                        300: '#66a3e0',
                        400: '#3385d6',
                        500: '#0066cc',
                        600: '#0052a3',
                        700: '#003d7a',
                        800: '#002952',
                        900: '#001429',
                    },
                    red: {
                        DEFAULT: '#d32f2f', // Primary red
                        dark: '#9a0007',
                        light: '#ff6659',
                        50: '#fde0dc',
                        100: '#f9bdbb',
                        200: '#f69988',
                        300: '#f27666',
                        400: '#ef5350',
                        500: '#f44336',
                        600: '#e53935',
                        700: '#d32f2f',
                        800: '#c62828',
                        900: '#b71c1c',
                    },
                    gray: {
                        50: '#f9fafb',
                        100: '#f3f4f6',
                        200: '#e5e7eb',
                        300: '#d1d5db',
                        400: '#9ca3af',
                        500: '#6b7280',
                        600: '#4b5563',
                        700: '#374151',
                        800: '#1f2937',
                        900: '#111827',
                    }
                }
            },
            fontFamily: {
                sans: ['Outfit', 'sans-serif'],
                display: ['Outfit', 'sans-serif'],
            },
            backgroundImage: {
                'hero-pattern': "url('/img/hero-pattern.svg')", // Placeholder
            },
            animation: {
                'fade-in-up': 'fadeInUp 0.8s ease-out forwards',
                'pulse-slow': 'pulse 3s infinite',
            },
            keyframes: {
                fadeInUp: {
                    '0%': { opacity: '0', transform: 'translateY(20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                }
            }
        },
    },
    plugins: [],
}
