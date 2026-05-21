import { TestCard } from "./TestCard"


export function TestsSection(){
    return (
    <div>
        <div className="relative w-full h-[600px] p-4">

            <div className="rounded-[40px] absolute inset-x-4 top-0 z-10 scale-[0.92] opacity-80 blur-[1px]">
                <TestCard
                title="Overlay test"
                text="Some text I want to display in this card in order to fill the space a
                bit because I do not want to add like 20 bilion padding in order to
                fill this space."
                date="24 October 2026"
                scoreBest="31/50"
                scoreLast="31/50"/>
            </div>
            <div className="rounded-[40px] absolute inset-x-0 top-40 z-20 opacity-100 scale-100 blur-0
            shadow-sm">
                <TestCard 
                title="My own test"
                text="
                Some text I want to display in this card in order to fill the space a
                bit because I do not want to add like 20 bilion padding in order to
                fill this space."
                date="11th June 2025"
                scoreBest="24/30"
                scoreLast="21/30"/>

            </div>

            <div className="rounded-[40px] absolute inset-x-4 top-70 z-10 scale-[0.92] opacity-80 blur-[1px]">
                <TestCard
                title="Math test"
                text="Some text I want to display in this card in order to fill the space a
                bit because I do not want to add like 20 bilion padding in order to
                fill this space."
                date="24 October 2026"
                scoreBest="31/50"
                scoreLast="31/50"/>
            </div>
            
           
            {/* <motion.div
            className="w-full absolute border border-zinc-200 top-[20%] left-0">
                Card2
            </motion.div>
            <motion.div
            className="w-full absolute border border-zinc-200 top-[40%] left-0">
                Card3
            </motion.div>
            <motion.div
            className="h-fullqe w-full absolute border border-zinc-200 top-1/2 left-0">
                Card4
            </motion.div> */}

        </div>        
    </div>
)
}