"use client"

import { motion } from "motion/react";
import { ButtonProps } from "./ButtonProps";
import { Button } from "./Button";
import { ExpandingArrow } from "../ExpandingArrow";


export function ButtonWithArrow({children, variant="primary"}: Readonly<ButtonProps>)
{
    return(
        <motion.div
        initial="initial"
        whileHover="hover">
            
            <Button variant={variant}>{children}
                <ExpandingArrow />
            </Button>

        </motion.div>
    );
}