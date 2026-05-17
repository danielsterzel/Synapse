
import Navbar from "@/app/components/layout/Navbar";
import { NotesDashboardPreview } from "./components/notes/NotesDashboardPreview";

import { ButtonWithArrow } from "./components/ui/Buttons/ButtonWithArrow";

export default function Page()
{

  return(
      <div className="flex flex-col min-h-screen">
          <Navbar />
        
        <section className="mt-32 ml-24">

        <div className="grid grid-cols-2">
            <div className="flex flex-col gap-12">
              
              <h1 className="text-6xl font-bold">
                Your AI powered workspace
              </h1>
              
              <p className="text-neutral-500 text-xl">
                An AI-powered workspace for learning, organizing knowledge,
                and generating contextual study materials.
              </p>

              <div className="flex gap-8">
                
                <ButtonWithArrow variant="primary">
                  Try out Synapse
                </ButtonWithArrow>

                <ButtonWithArrow variant="secondary">
                  See how it works
                </ButtonWithArrow>
              </div>
            </div>
            <div className="mr-6">
              <NotesDashboardPreview />
            </div>
          </div>
        </section>

  </div>)
}