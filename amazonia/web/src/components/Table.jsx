import { useState } from 'react';
import Tile from './Tile';
import styles from '../styles/Table.module.css';
import api from '../service/api';

export default function Table(props) {
  const tableSize = 8;

  const [clicksNumber, setClicksNumber] = useState(0);

  const handleClick = (id) => {
    setClicksNumber(clicksNumber + 1);
  };

  const findPath = async () => {
    //const { data } = await api.get('/products');
    const { data } = await api.get('/map');
    console.log(data);
  };

  const printTable = () => {
    const table = [];
    let index = 0;

    for (let row = 0; row < tableSize; row++) {
      for (let col = 0; col < tableSize; col++) {
        const tileColor = (row + col) % 2 === 0 ? '#000' : '#FFF';

        table.push(
          <Tile
            key={`${row}-${col}`}
            row={row}
            col={col}
            color={tileColor}
            index={index++}
            onCelulaClick={handleClick}
            clicksNumber={clicksNumber}
          />
        );
      }
    }

    return table;
  };

  return (
    <div className={styles.centralizar}>
      <div className={styles.table}>{printTable()}</div>
      <button className={styles.btnMap} onClick={findPath}>
        Encontrar Caminho
      </button>
    </div>
  );
}
