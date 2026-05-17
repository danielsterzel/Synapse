import { ListItem } from "../ui/ListItem";
import { Logo } from "@/app/components/layout/Logo";
import { Button } from "./Button";

export default function Navbar() {
    return (
        <nav className="w-full flex items-center justify-between px-8 py-6">

    <div className="flex items-center gap-16">
        <Logo />

        <ul className="flex items-center gap-6 list-none m-0 p-0">
            <ListItem href="#product">Product</ListItem>
            <ListItem href="#freatures">Features</ListItem>
            <ListItem href="#how-it-works">How it works</ListItem>
            <ListItem href="#workspace">Workspace</ListItem>
            <ListItem href="#pricing">Pricing</ListItem>
            <ListItem href="#faq">FAQ</ListItem>
        </ul>
    </div>

    <div className="flex items-center gap-4">
        <Button>Register</Button>

        <Button variant="secondary">
            Login
        </Button>
    </div>

</nav>
    );
}