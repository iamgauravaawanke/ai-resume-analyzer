
import Home from "./pages/Home";
import Results from "./pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
<BrowserRouter>

<Routes>



<Route
path=""
element={<Home/>}  />


<Route
path="/result"
element={<Results/>} />

</Routes>


</BrowserRouter>
  );
}

export default App;