"use client";

import { useState, useEffect } from "react";
import { NoteDashboardMenu } from "./NoteDashboardMenu";

import { AnimatePresence, motion } from "motion/react";
import { TopicsSection } from "./sections/TopicsSection";
import { UploadedSection } from "./sections/uploaded_section/UploadedSection";
import { TestsSection } from "./sections/test_section/TestsSection";
import { ContextSection } from "./sections/ContextSection";

const ANIMATION_DURATION = 0.6;

const sectionAnimation = {
    initial: {
        opacity: 0,
        filter: "blur(10px)",
        y: 10
    },

    animate: {
        opacity: 1,
        filter: "blur(0px)",
        y: 0,

        transition: {
            duration: ANIMATION_DURATION,
            ease: "easeInOut" as const
        }
    },

    exit: {
        opacity: 0,
        filter: "blur(10px)",
        y: -10,

        transition: {
            duration: ANIMATION_DURATION,
            ease: "easeInOut" as const
        }
    }
};

const sections = {

    // topics: TopicsSection,
    // uploaded: UploadedSection,
    // tests: TestsSection,
    context: ContextSection
} as const

type SectionKey = keyof typeof sections

const sectionKeys = Object.keys(sections) as Array<SectionKey>;


export function NotesDashboardPreview()
{   
    const [selected, setSelected] = useState<SectionKey>("context");
    
    useEffect(() => {

        const interval = setInterval(() => {
            setSelected((prev) => {
                
                const currentIndex = sectionKeys.indexOf(prev);
                const nextIndex = (currentIndex + 1) % sectionKeys.length;

                return sectionKeys[nextIndex];

            });
        }, 8000);

        return () => clearInterval(interval);

    }, []);

    const CurentSection = sections[selected];

    return (
        <div className="w-full select-none rounded-lg p-4">
            <div className="flex flex-col gap-2">
                <div className="flex flex-col items-center">
                    <div className="w-[50%] bg-neutral-200 rounded-lg  text-xs">
                        <NoteDashboardMenu selected={selected} 
                        animationDuration={ANIMATION_DURATION}/>
                    </div>
                </div>

                <AnimatePresence mode="wait">
                    <motion.div
                        key={selected}
                        variants={sectionAnimation}
                        initial="initial"
                        animate="animate"
                        exit="exit"
                        className="mt-4"
                    >

                    <CurentSection />
                    </motion.div>

                </AnimatePresence>

            </div>
        </div>
    );
}