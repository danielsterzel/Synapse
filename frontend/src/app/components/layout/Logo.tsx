export function Logo() {
    return (
        <div className="flex items-center gap-4">
            <svg
                width="48"
                height="48"
                viewBox="0 0 48 48"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                className="shrink-0"
            >
                <rect
                    x="10"
                    y="6"
                    width="26"
                    height="34"
                    rx="6"
                    className="fill-zinc-950"
                />

                <path
                    d="M18 17H28M18 23H31M18 29H25"
                    stroke="white"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                />

                <path
                    d="M35 12L36.4 15.6L40 17L36.4 18.4L35 22L33.6 18.4L30 17L33.6 15.6L35 12Z"
                    className="fill-fuchsia-500"
                />

                <circle cx="31" cy="31" r="2.5" className="fill-fuchsia-500" />
                <circle cx="38" cy="28" r="2.5" className="fill-fuchsia-500" />
                <circle cx="37" cy="36" r="2.5" className="fill-fuchsia-500" />

                <path
                    d="M33 30L36 29M32.5 32.5L35.5 35"
                    stroke="#d946ef"
                    strokeWidth="2"
                    strokeLinecap="round"
                />
            </svg>

            <span className="text-3xl font-bold tracking-tight text-zinc-950">
                Synapse
                <span className="ml-1 relative -top-1 text-fuchsia-500">.</span>
            </span>
        </div>
    );
}