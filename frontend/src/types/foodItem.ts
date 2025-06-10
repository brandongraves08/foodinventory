export interface FoodItem {
  id: string;
  name: string;
  category?: string;
  quantity?: number;
  unit?: string;
  expiration_date?: string;
  barcode?: string;
  image_url?: string;
  notes?: string;
  source?: string;
  created_at: string;
  updated_at: string;
  owner_id: string;
}

export interface FoodItemCreate {
  name: string;
  category?: string;
  quantity?: number;
  unit?: string;
  expiration_date?: string;
  barcode?: string;
  image_url?: string;
  notes?: string;
  source?: string;
}

export interface FoodItemUpdate {
  name?: string;
  category?: string;
  quantity?: number;
  unit?: string;
  expiration_date?: string;
  barcode?: string;
  image_url?: string;
  notes?: string;
}
