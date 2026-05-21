import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBuffer } from "@fortawesome/free-brands-svg-icons";
import { faFileLines } from "@fortawesome/free-regular-svg-icons";
import { faPencil } from "@fortawesome/free-solid-svg-icons";
import { faWater } from "@fortawesome/free-solid-svg-icons";
import { faHotjar } from "@fortawesome/free-brands-svg-icons";
import { faBolt } from "@fortawesome/free-solid-svg-icons";
import { faDumbbell } from "@fortawesome/free-solid-svg-icons";
import { faCommentDots } from "@fortawesome/free-regular-svg-icons";
import { faBoxOpen } from "@fortawesome/free-solid-svg-icons";
import { faSliders } from "@fortawesome/free-solid-svg-icons";
import { faPlus } from "@fortawesome/free-solid-svg-icons";
import { faMinus } from "@fortawesome/free-solid-svg-icons";

export function TopicsSection()
{
    return (
    <div className="w-full border border-zinc-200 rounded-lg p-4">
        
        <div className="flex items-center gap-4">
        <h1 className="text-xl tracking-wider">Topic </h1>
        <div className="w-full h-px flex 1 bg-neutral-300" />
        </div>
        <span className="mt-4 text-4xl text-netural-400 font-bold ">Physics</span>


        <div className=" flex gap-4 rounded-lg p-2">
            <div className="flex flex-col gap-1 items-center">
                <div className="
                    flex items-center justify-center
                    w-12 h-12 bg-purple-100 rounded-xl">
                    <FontAwesomeIcon icon={faCommentDots} className="text-purple-500"/>
                </div>
            <p className="text-xs tracking-wide text-neutral-500 uppercase text-center">AI Chat</p>

            </div>
            <div className="flex flex-col gap-1 items-center">
                
                <div className="
                flex items-center justify-center
                w-12 h-12 bg-yellow-100 rounded-xl">
                    <FontAwesomeIcon icon={faBuffer} className="text-orange-300"/>
                </div>
                <p className="text-xs tracking-wide text-neutral-500 uppercase text-center"> context</p>
            </div>
            <div className="flex flex-col gap-1 items-center">
                <div className="
                flex items-center justify-center w-12 h-12 
                bg-blue-100 rounded-xl">
                    <FontAwesomeIcon icon={faBoxOpen} className="text-blue-500"/>
                </div>
                <p className="text-xs tracking-wide text-neutral-500 uppercase text-center">docs</p>
            </div>
            <div className="flex flex-col gap-1 items-center">
                <div className="
                flex items-center justify-center w-12 h-12 
                bg-green-100 rounded-xl">
                    <FontAwesomeIcon icon={faFileLines} className="text-emerald-500"/>
                </div>
                <p className="text-xs tracking-wide text-neutral-500 uppercase text-center">Tests</p>
            </div>
            
        </div>
        <div className="flex flex-col gap-2 mt-4">
        <div className="flex justify-between items-center">
            <label className="text-md"><FontAwesomeIcon icon={faPencil}/>My notes</label>
            <div className="flex gap-2 mr-2">
                <button className="text-neutral-500  cursor-pointer">
                    <FontAwesomeIcon icon={faPlus}/>
                </button>
                <button className="text-neutral-500 cursor-pointer">
                    <FontAwesomeIcon icon={faSliders}/>
                </button>
            </div>
        </div>
        <ul className="flex flex-col gap-1 text-xs">


            <li className="h-full flex gap-4 border  border-zinc-200 rounded-lg ">
                
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faDumbbell}/>
                </div>

                <div className="w-full flex justify-between">
                    <div className="flex flex-col gap-1">
                        <p>Kinematics</p>
                        <p className="text-neutral-400">Last modified: 2 month ago</p>
                        <p className="text-neutral-400">Createad at 11 March 2025</p>
                    </div>
                    <FontAwesomeIcon icon={faMinus} className="cursor-pointer m-1 text-neutral-500"/>
                </div>
            </li>


            <li className="h-full flex gap-4  border border-zinc-200 rounded-lg ">
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faHotjar}/>    
                </div>
                <div className="w-full flex justify-between">
                    <div className="flex flex-col gap-1">
                        <p>Thermodynamics</p>
                        <p className="text-neutral-400">Last modified: 1 month ago</p>
                        <p className="text-neutral-400">Createad at 27 March 2025</p>
                    </div>
                    <FontAwesomeIcon icon={faMinus} className="cursor-pointer m-1 text-neutral-500"/>
                 </div>
            </li>


            <li className="h-full flex gap-4  border border-zinc-200 rounded-lg ">
                    <div className="
                        w-16 
                        border-r border-zinc-200
                        flex items-center justify-center">
                        <FontAwesomeIcon icon={faWater}/>
                    </div>
                    <div className="w-full flex justify-between">
                        <div className="flex flex-col gap-1">
                            <p>Waves and Oscillations</p>
                            <p className="text-neutral-400">Last modified: 3 weeks ago</p>
                            <p className="text-neutral-400">Createad at 14 April 2025</p>
                        </div>
                    <FontAwesomeIcon icon={faMinus} className="cursor-pointer m-1 text-neutral-500"/>
                    </div>
                </li>


            <li className="h-full flex gap-4  border border-zinc-200 rounded-lg ">
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faBolt}/>
                    
                </div>
                <div className="w-full flex justify-between">
                    <div className="flex flex-col gap-1">
                        <p>Electricity and Magnetism</p>
                        <p className="text-neutral-400">Last modified: 2 weeks ago</p>
                        <p className="text-neutral-400">Createad at 18 May 2025</p>
                    </div>
                <FontAwesomeIcon icon={faMinus} className="cursor-pointer m-1 text-neutral-500"/>
                </div>
            </li>
        </ul>
        </div>
    </div>
);
}