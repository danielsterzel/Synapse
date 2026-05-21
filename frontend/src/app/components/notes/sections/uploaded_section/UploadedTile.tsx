

type UploadedTileProps = {
    children: React.ReactNode
}


export function UploadedTile({children}: Readonly<UploadedTileProps>)
{
    return (
    
    <div className="
    
    aspect-square
    flex flex-col items-center justify-center w-fit rounded-xl p-2
     bg-blue-100 text-blue-500">
        {children}
    </div>
    );
}