import { useMemo } from "react";

const topics = [

    {
        key: "topics",
        label: "Topics"
    },
    {
        key: "uploaded",
        label: "Uploaded"
    },
    {
        key: "tests",
        label: "Tests"
    },
    {
        key: "context",
        label: "Context"
    }

 ] as const

 type SectionKey = typeof topics[number]["key"];

type NoteDashBoardMenuProps = {
    selected: SectionKey;
    animationDuration: number;
}

export function NoteDashboardMenu({ selected, animationDuration }: NoteDashBoardMenuProps)
{

    const durationMs = useMemo(() => {return animationDuration * 1000}, [animationDuration]);

    return (
        <ul className="flex gap-1 justify-between items-center m-1 px-1 text-xs">
            {topics.map((topic) => (
                <li
                    key={topic.key}
                    className={`
                     cursor-pointer rounded-md px-2 py-1 transition-colors
                        ${selected === topic.key
                            ? `bg-white text-black scale-[1.08] ease-in-out`
                            : ""}
                    `}
                    style={{
                      transitionDuration: `${durationMs}ms`
                    }}
                >
                    {topic.label}
                </li>
            ))}
        </ul>
    );
}

