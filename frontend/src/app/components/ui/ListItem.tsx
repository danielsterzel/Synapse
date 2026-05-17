"use client"

import {motion} from "motion/react";

type ListItemProps = {
    children: string
    href: string
};

type ReadonlyListItemProps = Readonly<ListItemProps>;

export function ListItem({children, href}: ReadonlyListItemProps) {
    return (
        <motion.li
            initial="initial"
            whileHover="hover"
            className={"relative text-md tracking-tight font-medium"}
        >

            <a href={href}>{children}</a>
            <motion.div
                variants={{
                    initial: {
                        scaleX: 0
                    },
                    hover: {
                        scaleX: 1
                    }
                }}
                transition={{duration: 0.3, ease:"easeOut"}}
                className="absolute bottom-0 
                left-0  origin-left h-px w-full bg-zinc-900"
            />
        </motion.li>
    )
}