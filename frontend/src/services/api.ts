import axios from 'axios';
import { FoodItem, FoodItemCreate } from '../types/foodItem';

const API_URL = '/api/v1';

// Configure axios
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Food Items API
export const foodItemsApi = {
  getAll: async (skip = 0, limit = 100): Promise<FoodItem[]> => {
    const response = await axios.get(`${API_URL}/food-items/`, {
      params: { skip, limit },
    });
    return response.data;
  },
  
  getById: async (id: string): Promise<FoodItem> => {
    const response = await axios.get(`${API_URL}/food-items/${id}`);
    return response.data;
  },
  
  create: async (foodItem: FoodItemCreate): Promise<FoodItem> => {
    const response = await axios.post(`${API_URL}/food-items/`, foodItem);
    return response.data;
  },
  
  update: async (id: string, foodItem: Partial<FoodItemCreate>): Promise<FoodItem> => {
    const response = await axios.put(`${API_URL}/food-items/${id}`, foodItem);
    return response.data;
  },
  
  delete: async (id: string): Promise<FoodItem> => {
    const response = await axios.delete(`${API_URL}/food-items/${id}`);
    return response.data;
  },
  
  getExpiringSoon: async (days = 7): Promise<FoodItem[]> => {
    const response = await axios.get(`${API_URL}/food-items/expiring-soon/`, {
      params: { days },
    });
    return response.data;
  },
};

// Barcode API
export const barcodeApi = {
  lookup: async (barcode: string): Promise<FoodItemCreate> => {
    const response = await axios.get(`${API_URL}/barcode/${barcode}`);
    return response.data;
  },
};

// Image Analysis API
export const imageAnalysisApi = {
  analyze: async (imageFile: File): Promise<FoodItemCreate> => {
    const formData = new FormData();
    formData.append('file', imageFile);
    
    const response = await axios.post(`${API_URL}/image-analysis/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    
    return response.data;
  },
};
