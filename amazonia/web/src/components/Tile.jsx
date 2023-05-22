/* eslint-disable react/prop-types */
import styles from '../styles/Tile.module.css';
import CircleIcon from '@mui/icons-material/Circle';
import { useState, useEffect } from 'react';

// eslint-disable-next-line react/prop-types
const Tile = ({
  id,
  onCelulaClick,
  row,
  col,
  checked,
  color,
  innerColor,
  size,
}) => {
  const [isChecked, setIsChecked] = useState(false);
  const [checkColor, setCheckColor] = useState(innerColor);

  const handleClick = () => {
    onCelulaClick(id, row, col);
    setIsChecked(!isChecked);
  };

  useEffect(() => {
    setIsChecked(checked);
    setCheckColor(innerColor);
  }, [checked, innerColor, isChecked]);

  return (
    <div
      className={styles.tile}
      style={{ backgroundColor: color }}
      onClick={handleClick}
    >
      {isChecked && (
        <CircleIcon style={{ color: checkColor, fontSize: size }} />
      )}
    </div>
  );
};

export default Tile;
