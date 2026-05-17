"use client";

import { useState, useEffect } from "react";
import { Tile } from "../ui/Tile";
import { StaggerList } from "../ui/StaggerList";
import { NoteDashboardMenu } from "./NoteDashboardMenu";
import { DashboardSection } from "./sections/DashboardSection";

import { AnimatePresence, motion } from "motion/react";

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



export function NotesDashboardPreview()
{   
    const [selected, setSelected] = useState(0);

    useEffect(() => {

        const interval = setInterval(() => {
            setSelected((prev) => (
                prev === 3 ? 0 : prev + 1
            ));
        }, 8000);

        return () => clearInterval(interval);

    }, []);

    return (
        <div className="w-full  rounded-lg p-4">
            <div className="flex flex-col gap-2">
                <div className="flex flex-col items-center">
                    <div className="w-[50%] bg-neutral-200 rounded-lg  text-xs">
                        <NoteDashboardMenu selected={selected} 
                        animationDuration={ANIMATION_DURATION}/>
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

                        <DashboardSection selected={selected}/>
                        </motion.div>

                    </AnimatePresence>


                </div>

            </div>
        </div>
    );
}