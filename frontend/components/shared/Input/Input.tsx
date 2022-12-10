import { FC } from "react";
import classNames from "classnames";
import { Input as AntInput } from "antd";

import { InputProps } from "antd/lib/input/Input";

import styles from "./Input.module.scss";

export const Input: FC<InputProps> = ({ className, ...restProps }) => {
  return (
    <AntInput className={classNames(styles.input, className)} {...restProps} />
  );
};
