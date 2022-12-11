import { FC } from "react";
import { Button as AntButton } from "antd";
import { ButtonProps } from "antd/lib/button/button";
import styles from "./PrimaryButton.module.scss";

export const Button: FC<ButtonProps> = ({ children }) => {
  return <AntButton className={styles.button}>{children}</AntButton>;
};
