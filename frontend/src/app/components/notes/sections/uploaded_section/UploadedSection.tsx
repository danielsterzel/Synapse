import { UploadedTile } from "./UploadedTile";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFile } from "@fortawesome/free-regular-svg-icons";
import { faPen } from "@fortawesome/free-solid-svg-icons";
import { Button } from "@/app/components/ui/Buttons/Button";

export function UploadedSection()
{
    return(
        
        <div className="flex flex-col gap-8 border border-zinc-200 rounded-lg p-4">
            <h1 className="text-3xl font-bold tracking-wide text-center text-pretty">
                Uploaded files
            </h1>
            <div className="grid grid-cols-3">
                
                <div className="flex flex-col gap-2 text-center 
                    items-center text-pretty text-lg">

                    <UploadedTile>
                        <FontAwesomeIcon icon={faFile}/>
                    </UploadedTile>
                    <label className="text-xs">Lecture_Notes.pdf</label>

                </div>
                
                <div className="flex flex-col gap-2 text-center 
                    items-center text-pretty text-lg">

                    <UploadedTile>
                        <FontAwesomeIcon icon={faFile}/>
                    </UploadedTile>
                    <label className="text-xs">TodoList.pdf</label>

                </div>               
                
                 <div className="flex flex-col gap-2 text-pretty text-center  
                    items-center justify-center  text-md">

                    <UploadedTile>
                        <FontAwesomeIcon icon={faFile}/>
                    </UploadedTile>
                        <label className="text-xs">ML_exam2025.pdf</label>
                </div>
            </div>


        </div>

    );
}