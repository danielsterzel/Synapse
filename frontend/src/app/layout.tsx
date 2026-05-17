
import { Metadata } from "next";
import { ReactNode } from "react";
import { Montserrat } from "next/font/google";
import "./globals.css"

export const metadata: Metadata = {
  title: "Synapse",
  description: "AI powered note taking app"
};

const montserrat = Montserrat({
  subsets: ["latin"]
});

export default function RootLayout({children}: Readonly<{children: ReactNode}>)
{
  return (<html lang="en">
  <body className={montserrat.className}>
    {children}
  </body>
  </html>)
}