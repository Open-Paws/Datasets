import pandas as pd
from pathlib import Path
from typing import List, Tuple, Dict

def load_nameusage_file(file_path: Path) -> pd.DataFrame:
    print(f"Loading NameUsage file from {file_path}")
    df = pd.read_csv(file_path, sep='\t', dtype=str, low_memory=False)
    print(f"Loaded {len(df)} rows from NameUsage file")
    print("Columns in the file:", df.columns.tolist())
    print("First few rows:")
    print(df.head().to_string())
    return df

def build_hierarchy(df: pd.DataFrame) -> pd.DataFrame:
    print("Building taxonomy hierarchy")
    
    # Check for required columns
    required_columns = ['col:ID', 'col:parentID', 'col:scientificName', 'col:rank']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Error: Missing required columns: {missing_columns}")
        return df

    print("Creating dictionary for quick lookups")
    df_dict = df.set_index('col:ID').to_dict('index')
    print(f"Dictionary created with {len(df_dict)} entries")
    
    def get_hierarchy(row_id: str) -> List[Tuple[str, str]]:
        print(f"Starting hierarchy for ID: {row_id}")
        hierarchy: List[Tuple[str, str]] = []
        current_id = row_id
        visited = set()
        while current_id and current_id in df_dict and current_id not in visited:
            visited.add(current_id)
            row = df_dict[current_id]
            name = row['col:scientificName']
            rank = row['col:rank']
            if name and rank:
                hierarchy.append((name, rank))
                print(f"  Added to hierarchy: {name} ({rank})")
            current_id = row['col:parentID']
            print(f"  Next parent ID: {current_id}")
        print(f"Completed hierarchy for ID: {row_id}")
        return list(reversed(hierarchy))

    # Check the number of rows where rank is 'species'
    species_rows = df['col:rank'].str.lower() == 'species'
    print(f"Rows with rank 'species': {species_rows.sum()}")

    print("Building hierarchies for rows with rank 'species'")
    # Only build hierarchy for rows where rank is 'species'
    df['hierarchy'] = df.apply(lambda row: get_hierarchy(row['col:ID']) if row['col:rank'].lower() == 'species' else [], axis=1)
    
    print("Extracting taxonomic ranks")
    # Extract taxonomic ranks
    ranks = ['kingdom', 'phylum', 'subphylum', 'class', 'subclass', 'order', 'suborder', 
             'superfamily', 'family', 'subfamily', 'tribe', 'subtribe', 'genus', 'subgenus', 
             'section', 'species']
    for rank in ranks:
        print(f"Extracting {rank}")
        df[f'col:{rank}'] = df['hierarchy'].apply(
            lambda h: next((name for name, r in h if r.lower() == rank), None)
        )
    
    hierarchies_built = len(df[df['hierarchy'].str.len() > 0])
    print(f"Hierarchy built for {hierarchies_built} rows")
    
    if hierarchies_built == 0:
        print("Warning: No hierarchies were built. Checking data:")
        print(df[['col:ID', 'col:parentID', 'col:scientificName', 'col:rank']].head().to_string())
    else:
        print("Sample of rows with built hierarchies:")
        print(df[df['hierarchy'].str.len() > 0].head().to_string())
    
    return df

def filter_animalia(df: pd.DataFrame) -> pd.DataFrame:
    print("Filtering for Animalia kingdom")
    df_animalia = df[df['col:kingdom'] == 'Animalia']
    print(f"Filtered to {len(df_animalia)} rows in Animalia kingdom")
    if len(df_animalia) == 0:
        print("Warning: No rows found for Animalia kingdom. Checking unique kingdom values:")
        print(df['col:kingdom'].unique())
    else:
        print("Sample of Animalia rows:")
        print(df_animalia.head().to_string())
    return df_animalia

def main():
    try:
        # Adjust the file path as needed
        file_path = Path.home() / "Desktop" / "COL_ORIGINAL" / "NameUsage.tsv"
        
        df = load_nameusage_file(file_path)
        df_with_hierarchy = build_hierarchy(df)
        df_animalia = filter_animalia(df_with_hierarchy)
        
        # Select columns to keep in the output
        ranks = ['kingdom', 'phylum', 'subphylum', 'class', 'subclass', 'order', 'suborder', 
                 'superfamily', 'family', 'subfamily', 'tribe', 'subtribe', 'genus', 'subgenus', 
                 'section', 'species']
        columns_to_keep = ['col:ID', 'col:scientificName', 'col:rank'] + [f'col:{rank}' for rank in ranks]
        df_output = df_animalia[columns_to_keep]
        
        output_path = Path.home() / "Desktop" / "animalia_hierarchy.tsv"
        df_output.to_csv(output_path, sep='\t', index=False)
        print(f"Animalia hierarchy saved to: {output_path}")
        print(f"Number of rows in output file: {len(df_output)}")
        print("Sample of output data:")
        print(df_output.head().to_string())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()