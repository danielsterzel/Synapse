"use client";

import { motion } from "motion/react";

const pathVariant = {
    initial: {
        d: "M20 12 L20 12",
        strokeWidth: 2
    },

    hover: {
        d: "M6 12 L20 12",
        strokeWidth: 3
    }
};

const arrowVariant = {
    initial: {
        strokeWidth: 2
    },

    hover: {
        strokeWidth: 3
    }
};

export function ExpandingArrow()
{
    return (
        <div
        >
            <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
            >
                <motion.path
                    d="M20 12 L20 12"
                    variants={pathVariant}
                    transition={{
                        duration: 0.3,
                        ease: "easeOut"
                    }}
                    stroke="currentColor"
                    strokeLinecap="round"
                />

                <motion.path
                    d="M14 6 L20 12 L14 18"
                    variants={arrowVariant}
                    transition={{
                        duration: 0.3,
                        ease: "easeOut"
                    }}
                    stroke="currentColor"
                    strokeLinecap="round"
                />
            </svg>
        </div>
    );
}