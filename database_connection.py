import pyodbc
import pandas as pd
from llama_index.core.tools.tool_spec.base import BaseToolSpec

class GaleriTools(BaseToolSpec):
    """Galeri Sistemi Veritabanı Bağlantıları ve Sorguları"""

    spec_functions = ["get_car", "add_car", "update_car_price", "delete_car"]

    def __init__(self, server, database) -> None:
        """MS SQL bağlantısını başlatır."""
        self.conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        self.connection = pyodbc.connect(self.conn_str)

    def get_car(self) -> pd.DataFrame:
        """Tüm arabalaro getirir."""

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM arabalar")
        rows = cursor.fetchall()
        return rows  # Pandas DataFrame yerine direkt liste döndürüyoruz.

    def add_car(self, marka: str, model: str, yil: int, fiyat: int, renk: str,plaka: str):
        """Yeni çalışan ekler."""

        query = "INSERT INTO arabalar (marka, model, yil, fiyat, renk, plaka) VALUES (?, ?, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(query, (marka, model, yil, fiyat, renk, plaka))
        self.connection.commit()
        return f"{marka} {model} {yil} başarıyla eklendi."

    def update_car_price(self, marka: str, model: str, yeni_fiyat: int):
        """Çalışanın maaşını günceller."""
        query = "UPDATE arabalar SET fiyat = ? WHERE marka = ? AND model = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (yeni_fiyat, marka, model))
        self.connection.commit()
        return f"{marka} {model} aracı fiyatı {yeni_fiyat} olarak güncellendi."

    def delete_car(self, marka: str, model: str):
        """Çalışanı siler."""
        query = "DELETE FROM arabalar WHERE marka = ? AND model = ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (marka,model,))
        self.connection.commit()
        return f"{marka} {model} aracı başarıyla silindi."

