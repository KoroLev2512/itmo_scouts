import { FC } from "react";
import { ButtonProps } from "antd/lib/button/button";
import styles from "./Button.module.scss";
import { Button } from "./Button";

export const PrimaryButton: FC<ButtonProps> = ({ children }) => {
  return <Button className={styles.button}>{children}</Button>;
};
