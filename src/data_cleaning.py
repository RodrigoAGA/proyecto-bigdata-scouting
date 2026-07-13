"""Funciones de parsing reutilizables para el dataset merged_players.csv."""

import re
from typing import Optional

import pandas as pd


def parse_height_cm(value: str) -> Optional[float]:
    """Convierte alturas tipo 5'9" a centimetros."""
    if not isinstance(value, str):
        return None
    match = re.match(r"(\d+)'(\d+)\"?", value.strip())
    if not match:
        return None
    feet, inches = int(match.group(1)), int(match.group(2))
    return round((feet * 12 + inches) * 2.54, 1)


def parse_weight_kg(value: str) -> Optional[float]:
    """Convierte pesos tipo '65 kg' a numero."""
    if not isinstance(value, str):
        return None
    match = re.match(r"(\d+)\s*kg", value.strip())
    return float(match.group(1)) if match else None


def parse_currency(value: str) -> Optional[float]:
    """Convierte valores tipo '0$' a numero."""
    if not isinstance(value, str):
        return None
    cleaned = re.sub(r"[^\d.]", "", value)
    return float(cleaned) if cleaned else None


def clean_players(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica el parsing basico a las columnas conocidas del dataset."""
    df = df.copy()
    df["Height_cm"] = df["Height"].apply(parse_height_cm)
    df["Weight_kg"] = df["Weight"].apply(parse_weight_kg)
    df["Transfer_Value_num"] = df["Transfer Value"].apply(parse_currency)
    return df
