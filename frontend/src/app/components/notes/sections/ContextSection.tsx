"use client";
import {motion} from "motion/react";

import { faBoxOpen } from "@fortawesome/free-solid-svg-icons";
import { faPen } from "@fortawesome/free-solid-svg-icons";
import { faStar } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

// TODO: improve graphics
export function ContextSection()
{
    return(
    <div className="flex flex-col gap-4">
        <h1 className="font-bold text-2xl">Topic context</h1>
        <p className="text-neutral-500 text-md text-pretty">Personalize context in topic 
            to help AI agent give you the best notes and most insightful tests
        </p>
        <div className="flex flex-col justify-center items-center">
            <FontAwesomeIcon icon={faBoxOpen} className=" text-orange-400 text-6xl"/>
            <div className="relative w-full mt-2 flex flex-col gap-2 justify-center items-center">
                <h2 className="text-xl font-semibold">Current Context</h2>
                
                <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: 256 }}
                    transition={{ duration: 0.5, ease: "easeOut" }}
                    className="h-px bg-neutral-500 rounded-full"
                />
                <div className="flex justify-between text-sm gap-4">

                   <button
                        className="
                            flex items-center gap-2
                            rounded-full px-3 py-1
                            hover:bg-neutral-200
                            transition-colors duration-200
                            cursor-pointer
                        "
                        >
                        <div className="w-3 h-3 rounded-full bg-violet-500" />
                        <span>Change context with AI</span>
                        </button>


                    <button
                            className="
                                flex items-center gap-2
                                rounded-full px-3 py-1
                                hover:bg-neutral-200
                                transition-colors duration-200
                                cursor-pointer
                            "
                            >
                            <div className="w-3 h-3 rounded-full bg-red-500" />
                            <span>Remove context</span>
                    </button>
                </div>
                <div className="relative flex flex-col gap-1 bg-gradient-to-br from-neutral-100 to-neutral-50
                        rounded-lg p-4">
                    <div className="flex gap-1 items-center absolute top-2 right-2">
                        <FontAwesomeIcon icon={faPen} className="cursor-pointer"/>
                        <FontAwesomeIcon icon={faStar} className="cursor-pointer"/>
                    </div>
                <p className="text-sm  text-neutral-500 whitespace-pre-line">
                    {`
                    User is preparing for a university-level Calculus exam.

                    Current weaknesses:
                     [ Integration by parts ]
                     [ Differential equations ]
                     [ Trigonometric substitutions ]

                    The user prefers concise but deep explanations with visual intuition.

                    Generate challenging tests with mixed problem types and detailed feedback.

                    Focus on understanding concepts instead of memorization.
                    `}
                    </p>
                </div>
            </div>
        </div>
    </div>

    );
}