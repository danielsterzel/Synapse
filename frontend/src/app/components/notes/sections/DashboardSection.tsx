import { TopicsSection } from "./TopicsSection"
import { UploadedSection } from "./UploadedSection"
import { TestsSection } from "./TestsSection"
import { ContextSection } from "./ContextSection"

type Props = {
    selected: number
}


export function DashboardSection({selected}: Props)
{


    switch(selected){
        case 0:
            return <TopicsSection />
            
        case 1:
            return <UploadedSection /> 
        case 2:
            return <TestsSection />
        case 3: 
        return <ContextSection />
    }


}