import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import HotelsPage from "./pages/HotelsPage";
import Navbar from "./components/Navbar";
import ChatPage from "./pages/ChatPage";
import BookingPage from "./pages/BookingPage";
import PaymentPage from "./pages/PaymentPage";
import BookingHistory from "./pages/BookingHistory";
import ProtectedRoute from "./components/ProtectedRoute";
function App() {

    return (

        <BrowserRouter>
            <Navbar />
            <Routes>
                

                <Route path="/" element={<Home />} />

                <Route path="/login" element={<Login />} />

                <Route path="/register" element={<Register />} />

                <Route path="/hotels" element={<HotelsPage />} />

                <Route path="/chat" element={<ChatPage />} />

                <Route path="/booking"

                    element={
                      <ProtectedRoute>

                      <BookingPage />

                      </ProtectedRoute>
                    }
                />

                 <Route
          path="/payment/:bookingId"
          element={<PaymentPage />}
        />

                <Route path="/bookings" element={
                    <ProtectedRoute>

                    <BookingHistory />

                    </ProtectedRoute>
                    }
               />

            </Routes>

        </BrowserRouter>
    );
}

export default App;