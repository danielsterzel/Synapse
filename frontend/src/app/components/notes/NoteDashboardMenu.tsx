import { useMemo } from "react";

const topics = [
    "Topics",
    "Uploaded",
    "Tests",
    "Context"
];

type Props = {
    selected: number;
    animationDuration: number;
}

export function NoteDashboardMenu({ selected, animationDuration }: Props)
{

    const durationMs = useMemo(() => {return animationDuration * 1000}, [animationDuration]);

    return (
        <ul className="flex gap-1 justify-between items-center m-1 px-1 text-xs">
            {topics.map((topic, index) => (
                <li
                    key={topic}
                    className={`
                     cursor-pointer rounded-md px-2 py-1 transition-colors
                        ${selected === index
                            ? `bg-white text-black scale-[1.08] ease-in-out`
                            : ""}
                    `}
                    style={{
                      transitionDuration: `${durationMs}ms`
                    }}
                >
                    {topic}
                </li>
            ))}
        </ul>
    );
}

