import React, { FC } from "react";
import { Input } from "../shared/Input";

import styles from "./style.module.scss";

export type Field = {
  label: string;
  name?: string;
  placeholder?: string;
};

type Props = {
  title: string;
  description: string;
  fields: Field[];
};

export const Step: FC<Props> = ({ description, title, fields }) => {
  return (
    <div className={styles.step}>
      <div className={styles.title}>{title}</div>
      <div className={styles.description}>{description}</div>
      <div className={styles.fields}>
        {fields.map((field, index) => (
          <div className={styles.field} key={index}>
            {field.label}
            <Input name={field.name} placeholder={field.placeholder} />
          </div>
        ))}
      </div>
    </div>
  );
};
