import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBuffer } from "@fortawesome/free-brands-svg-icons";
import { faFileLines } from "@fortawesome/free-regular-svg-icons";
import { faPencil } from "@fortawesome/free-solid-svg-icons";
import { faWater } from "@fortawesome/free-solid-svg-icons";
import { faHotjar } from "@fortawesome/free-brands-svg-icons";
import { faBolt } from "@fortawesome/free-solid-svg-icons";
import { faDumbbell } from "@fortawesome/free-solid-svg-icons";

export function TopicsSection()
{
    return (
    <div className="w-full">

        <div className="flex gap-4 items-start justify-start">

            <h1 className="text-2xl tracking-wider">Topic: </h1>
            <span className="text-3xl text-netural-400 font-bold">Physics</span>

        </div>
        <div className="w-[30%] grid grid-cols-2 rounded-lg p-2">
            <div className="flex flex-col gap-1 items-center">
                <div className="
                flex items-center justify-center
                w-12 h-12 bg-yellow-100 rounded-xl">
                    <FontAwesomeIcon icon={faBuffer} className="text-orange-300"/>
                </div>
                <p className="text-xs tracking-wide text-neutral-500 uppercase">context</p>
            </div>
            <div className="flex flex-col gap-1 items-center">
                <div className="
                flex items-center justify-center w-12 h-12 
                bg-green-100 rounded-xl">
                    <FontAwesomeIcon icon={faFileLines} className="text-emerald-500"/>
                </div>
                <p className="text-xs tracking-wide text-neutral-500 uppercase">Tests</p>
            </div>
        </div>
        <div className="flex flex-col gap-2 mt-4">
        <label className="text-md">My notes<FontAwesomeIcon icon={faPencil}/></label>
        <ul className="flex flex-col gap-1 text-xs">
            <li className="h-full flex gap-4 border border-zinc-200 rounded-lg ">
                
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faDumbbell}/>
                </div>

                <div className="flex flex-col gap-1">
                    <p>Kinematics</p>
                    <p className="text-neutral-400">Last modified: 2 month ago</p>
                    <p className="text-neutral-400">Createad at 11 March 2025</p>
                </div>
            </li>
            <li className="h-full flex gap-4 border border-zinc-200 rounded-lg ">
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faHotjar}/>    
                </div>
                <div className="flex flex-col gap-1">
                    <p>Thermodynamics</p>
                    <p className="text-neutral-400">Last modified: 1 month ago</p>
                    <p className="text-neutral-400">Createad at 27 March 2025</p>
                </div>
            </li>
            <li className="h-full flex gap-4 border border-zinc-200 rounded-lg ">
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faWater}/>
                </div>
                <div className="flex flex-col gap-1">
                    <p>Waves and Oscillations</p>
                    <p className="text-neutral-400">Last modified: 3 weeks ago</p>
                    <p className="text-neutral-400">Createad at 14 April 2025</p>
                </div>
                </li>
            <li className="h-full flex gap-4 border border-zinc-200 rounded-lg ">
                <div className="
                    w-16 
                    border-r border-zinc-200
                    flex items-center justify-center">
                    <FontAwesomeIcon icon={faBolt}/>
                    
                </div>
                <div className="flex flex-col gap-1">
                    <p>Electricity and Magnetism</p>
                    <p className="text-neutral-400">Last modified: 2 weeks ago</p>
                    <p className="text-neutral-400">Createad at 18 May 2025</p>
                </div>
            </li>
        </ul>
        </div>
    </div>
);
}