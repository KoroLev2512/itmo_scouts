import Head from "next/head";
import { Button } from "../components/shared/Button";

export default function Home() {
  return (
    <div>
      <Head>
        n<title>ITMO.SCOUTS</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Button />
      </main>
    </div>
  );
}
