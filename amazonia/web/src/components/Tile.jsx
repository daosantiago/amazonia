import { useState } from 'react';
import styles from '../styles/Tile.module.css';
export default function Tile({ index, color, clicksNumber, onCelulaClick }) {
  const colors = ['#1fa32a', '#d6e225', '#bd1e1e'];

  const [tileColor, setTileColor] = useState(color);

  const handleClick = () => {
    if (clicksNumber <= 2) {
      setTileColor(colors[clicksNumber]);
      onCelulaClick(index);
    }
  };
  return (
    <div
      className={styles.tile}
      style={{ backgroundColor: tileColor }}
      onClick={handleClick}
    ></div>
  );
}
