import { FC } from "react";
import { ButtonProps } from ".";
import styles from "./Button.module.scss";

export const Button: FC<ButtonProps> = (props) => {
  return <button className={styles.wrapper} {...props}></button>;
};
