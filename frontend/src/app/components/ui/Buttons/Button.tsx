
import type { ButtonProps } from "./ButtonProps";

export function Button({children, variant = "primary"}: Readonly<ButtonProps>)
{
    const baseStyles =
        "shadow-md px-12 py-2 rounded-full transition-all duration-300 cursor-pointer";

    const variants = {
        primary:
            "bg-gradient-to-r from-fuchsia-500 to-violet-500 text-white",

        secondary:
            "border border-zinc-300"
    };

    return (
        <button className={`${baseStyles} ${variants[variant]} flex items-center gap-2`}>
            {children}
        </button>
    );
}