import Navbar from "../components/Navbar"
import Hero  from "../components/Hero"
import UploadCard from "../components/UploadCard"

// import ResumeUpload from "../components/ResumeUpload"

function Home() {
    return(
<div className="min-h-screen bg-gradient-to-b from-slate-50 via-blue-50 to-white">

            <Navbar/>
            <Hero/>
            <UploadCard/>

               {/* <ResumeUpload /> */}
        </div>
    )
}

export default Home;