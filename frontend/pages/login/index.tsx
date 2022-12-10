import React, { useState } from "react";
import Layout from "./layout";

import styles from "./index.module.scss";
import { Field, Step } from "../../components/Login";

const STEPS = [
  {
    title: "Аккаунт компании",
    description: "Добавьте информацию о компании",
    fields: [{ label: "Название компании" }, { label: "ИНН" }],
  },
];
export default function Login() {
  const [step, setStep] = useState(STEPS[0]);

  return (
    <Layout className={styles.wrapper}>
      <div className={styles.form}>
        <Step {...step} />
      </div>
      <div className={styles.banner}></div>
    </Layout>
  );
}
