
type TileProps = {

    children: React.ReactNode
}

export function Tile({children}: Readonly<TileProps>)
{

    return (
    <div className={`
        flex items-center justify-start
        p-4 w-full h-full
        border border-neutral-200
        rounded-3xl`}>
        {children}

    </div>
);
}