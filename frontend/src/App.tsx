import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { useAuth } from './contexts/AuthContext';

// Pages
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import FoodItemsList from './pages/FoodItemsList';
import FoodItemDetail from './pages/FoodItemDetail';
import AddFoodItem from './pages/AddFoodItem';
import BarcodeScanner from './pages/BarcodeScanner';
import ImageAnalysis from './pages/ImageAnalysis';
import Layout from './components/Layout';

// Create theme
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

// Protected route component
const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return <>{children}</>;
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={
          <ProtectedRoute>
            <Layout />
          </ProtectedRoute>
        }>
          <Route index element={<Dashboard />} />
          <Route path="food-items" element={<FoodItemsList />} />
          <Route path="food-items/:id" element={<FoodItemDetail />} />
          <Route path="add-food-item" element={<AddFoodItem />} />
          <Route path="barcode-scanner" element={<BarcodeScanner />} />
          <Route path="image-analysis" element={<ImageAnalysis />} />
        </Route>
      </Routes>
    </ThemeProvider>
  );
}

export default App;
