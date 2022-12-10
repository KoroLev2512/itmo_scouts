import { FC, PropsWithChildren } from "react";

export const Layout: FC<PropsWithChildren<{}>> = ({ children }) => {
  return <div>{children}</div>;
};

export default Layout;
