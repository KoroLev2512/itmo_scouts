import classNames from "classnames";

import { FC, PropsWithChildren } from "react";
import styles from "./layout.module.scss";

export const Layout: FC<PropsWithChildren<{ className: string }>> = ({
  children,
  className,
}) => {
  return (
    <div className={classNames(styles.wrapper, className)}>{children}</div>
  );
};

export default Layout;
