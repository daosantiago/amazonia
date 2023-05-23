import { useState } from 'react';
import Tile from './Tile';
import styles from '../styles/Table.module.css';
import api from '../api/api';

const Table = () => {
  const tableSize = 8;
  const [tiles, setTiles] = useState([]);
  const colors = ['#1fa32a', '#d6e225', '#bd1e1e'];
  const [checkpoints, setCheckpoints] = useState([]);

  const create = () => {
    setCheckpoints([]);
    let index = 1;
    const newTiles = [];
    for (let row = 0; row < tableSize; row++) {
      for (let col = 0; col < tableSize; col++) {
        const color = (row + col) % 2 === 0 ? '#000' : '#FFF';
        newTiles.push({
          id: index++,
          row: row,
          col: col,
          color: color,
          checked: false,
          size: 0,
        });
      }
    }
    setTiles(newTiles);
  };

  const find = async () => {
    if (checkpoints.length < 3) return;

    const { data } = await api.post('map/', checkpoints);
    const path = data.path;

    const newTiles = tiles.map((tile) => {
      for (let i = 0; i < path.length; i++) {
        if (tile.id === path[i][0]) {
          for (let j = 0; j < checkpoints.length; j++) {
            const checkpoint = checkpoints[j];
            if (tile.row === checkpoint.row && tile.col === checkpoint.col) {
              return {
                ...tile,
                innerColor: colors[j],
                checked: true,
                size: 40,
              };
            }
          }
          return { ...tile, innerColor: '#dcdcdc', checked: true, size: 30 };
        }
      }
      return tile;
    });
    setCheckpoints([]);
    setTiles(newTiles);
  };

  const handleClick = (id, row, col) => {
    if (checkpoints.length < 3) {
      const newCheck = { id: id, row: row, col: col };

      setCheckpoints([...checkpoints, newCheck]);

      const newTiles = tiles.map((tile) => {
        if (tile.id === id) {
          return { ...tile, checked: true, size: 30 };
        }
        return tile;
      });

      setTiles(newTiles);
    }
  };

  return (
    <>
      <div>
        <h1>DRONEZONIA</h1>
      </div>
      <div className={styles.mapContainer}>
        <h2>
          - Clique no botão criar tabela.
          <br />
          - Depois clique em 3 pontos na tabela <br />- Clique em Buscar caminho
        </h2>
        <div className={styles.centralizar}>
          <div className={styles.table}>
            {tiles.map((tile) => (
              <Tile
                key={tile.id}
                id={tile.id}
                row={tile.row}
                col={tile.col}
                color={tile.color}
                innerColor={tile.innerColor}
                checked={tile.checked}
                size={tile.size}
                onCelulaClick={handleClick}
                clicks={checkpoints.length}
              />
            ))}
          </div>
        </div>
        <div className={styles.buttons}>
          <button className={styles.btn} onClick={create}>
            Criar tabela
          </button>
          <button className={styles.btn} onClick={find}>
            Buscar caminho
          </button>
        </div>
      </div>
    </>
  );
};

export default Table;
