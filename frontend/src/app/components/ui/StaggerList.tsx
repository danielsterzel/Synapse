"use client";

import { motion } from "motion/react";
import React from "react";

type StaggerListProps = {
    children: React.ReactNode
}

export function StaggerList({children}: Readonly<StaggerListProps>)
{
    const container = {
        hidden: {},
        show: {
            transition: {
                staggerChildren: 0.08
                }
            }   
        }
        const item = {
            hidden: {
                opacity: 0,
                y: 10
            },
            show: {
                opacity: 1,
                y: 0
            }
        }

        return (
            <motion.ul
                variants={container}
                initial="hidden"
                animate="show">
                    {React.Children.map(children, (child) => (
                        <motion.li variants={item}>
                            {child}
                        </motion.li>
                    ))}
    

            </motion.ul>
        );
}