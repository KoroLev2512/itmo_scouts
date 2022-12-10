import { JwtPayload } from 'jsonwebtoken';
const jwt = require('jsonwebtoken');

export const decodeJWT = (payload: string) => {
  try {
    return jwt.verify(payload, process.env.JWT_TOKEN);
  } catch (error) {
    console.log(error);
    return;
  }
};

export const signJWT = (payload: JwtPayload) => {
  return jwt.sign(payload, process.env.JWT_TOKEN, { expiresIn: '3600s' });
};
