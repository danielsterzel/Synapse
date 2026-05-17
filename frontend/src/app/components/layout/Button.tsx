
type ButtonProps = {
    children: React.ReactNode;
    variant?: "primary" | "secondary"
}


export function Button({children, variant = "primary"}: ButtonProps)
{
    const baseStyles =
        "shadow-md px-12 py-2 rounded-full transition-all duration-300 cursor-pointer hover:scale-[1.02]";

    const variants = {
        primary:
            "bg-gradient-to-r from-fuchsia-500 to-violet-500 text-white",

        secondary:
            "border border-zinc-300 hover:bg-zinc-100"
    };

    return (
        <button className={`${baseStyles} ${variants[variant]}`}>
            {children}
        </button>
    );
}