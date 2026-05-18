"use client";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFileText } from "@fortawesome/free-regular-svg-icons";
import { faCalendarDay } from "@fortawesome/free-solid-svg-icons";
import { faChartColumn } from "@fortawesome/free-solid-svg-icons";
import { faBookmark } from "@fortawesome/free-regular-svg-icons";
import { motion } from "motion/react";

type TestCardProps = {
    title: string;
    text: string;
    date: string
    scoreBest: string
    scoreLast: string
}

export function TestCard({title, text, date, scoreBest, scoreLast} : Readonly<TestCardProps>) {
  return (
    <motion.div
    whileHover={{
        scale: 1.01
    }}
    transition={{
        duration: 0.3
    }}

     className="bg-white p-4 border border-zinc-400 rounded-[40px]">
      <div className="flex gap-2 items-center">
        <FontAwesomeIcon icon={faFileText} className="text-green-600" />
        <p className="text-xl font-bold">Test: {title}</p>
      </div>

      <div className="bg-green-600 h-px w-full m-1" />

      <div className="w-full">
        <p className="tracking-wide text-md text-pretty break-words overflow-hidden">
                {text}
        </p>

        <div className="mt-2 w-full text-md text-neutral-500 flex justify-between items-center">
          <div className="flex flex-col items-center justify-center gap-1">
            <p>Created: {date}</p>
            <FontAwesomeIcon icon={faCalendarDay} />
          </div>
          <div className="flex flex-col items-center justify-center gap-1">
            <p>Best score: {scoreBest}</p>
            <FontAwesomeIcon icon={faChartColumn} />
          </div>
          <div className="flex flex-col items-center justify-center gap-1">
            <p>Last score:{scoreLast}</p>
            <FontAwesomeIcon icon={faBookmark} />
          </div>
        </div>
      </div>
    </motion.div>
  );
}
