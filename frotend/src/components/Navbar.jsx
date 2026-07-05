import { Button } from "../components/ui/button"



function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b bg-white/90 backdrop-blur-md shadow-sm">
      <div className="container mx-auto flex h-16 items-center justify-between px-6">

        {/* Logo */}
        <div>
<h1 className="text-4xl font-extrabold text-blue-600 tracking-tight">
  ResumeAI
          </h1>
        </div>

        {/* Navigation */}
        <nav className="flex items-center gap-8">
          <a
            href="#"
            className="text-sm font-medium text-gray-600 transition hover:text-blue-600"
          >
            Home
          </a>

          <a
            href="#"
            className="text-sm font-medium text-gray-600 transition hover:text-blue-600"
          >
            About
          </a>

          <Button size="sm">
            Analyze Resume
          </Button>


          <Button className="bg-blue-600 hover:bg-blue-700">
  Get Started
</Button>
        </nav>

      </div>
    </header>
  );
}

export default Navbar;